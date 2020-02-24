import { createContext, h } from 'preact';
import { useReducer } from 'preact/hooks';
import { Route, Switch, useLocation } from 'wouter-preact';

import Login from './routes/login';
import Home from './routes/home';
import Register from "./routes/register";


export const AuthContext = createContext({});
const initialState = {
	isAuthenticated: false,
	token: null,
	user: null
};

const reducer = (state, action) => {
	switch (action.type) {
		case 'login':
			localStorage.setItem('user', JSON.stringify(action.payload.user));
			localStorage.setItem('token', JSON.stringify(action.payload.access_token));
			return {
				...state,
				isAuthenticated: true,
				user: action.payload.user,
				token: action.payload.token
			};
		case 'logout':
			localStorage.clear();
			return {
				...state,
				isAuthenticated: false,
				user: null,
				token: null
			};
		default: return state;
	}
};

const App = () => {
	const [state, dispatch] = useReducer(reducer, initialState);
	const [, setLocation] = useLocation();

	return (
		<AuthContext.Provider value={{ state, dispatch }}>
			<div className="app">
				{!state.isAuthenticated ? setLocation('/app/login') : setLocation('/app/')}
			</div>


			<Switch>
				<Route path="/app/"> <Home /> </Route>
				<Route path="/app/login"> <Login /> </Route>
			</Switch>
		</AuthContext.Provider>
	);
};

export default App;
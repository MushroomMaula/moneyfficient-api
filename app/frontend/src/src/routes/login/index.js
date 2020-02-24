import { h } from 'preact';
import { useState } from 'preact/hooks';
import { api } from '../../services/auth';
import { useContext } from 'preact/compat';
import { AuthContext } from '../../index';
import {Link} from "wouter-preact";


const Login = () => {
	// default form state
	const initialState = {
		email: '',
		password: '',
		isSubmitting: false,
		errorMessage: null
	};
	const [data, setData] = useState(initialState);
	const { dispatch } = useContext(AuthContext);
	function handleDataChange( event ) {
		event.preventDefault();
		// use the name property the of the input field to change the data
		setData({ ...data, [event.target.name]: event.target.value });
	}

	async function handleSubmit( event ) {
		event.preventDefault();
		setData({ ...data, isSubmitting: true, errorMessage: null });
		// call auth server
		api.login(data)
			// dispatch successful login to AuthContext
			.then(
				res => {
					dispatch({
						type: 'login',
						payload: res
					});
				}
			)
			// catch possible Login Error
			.catch(
				error => {
					console.log(error);
					console.log(error.message, error.statusText);
					setData({ ...data, errorMessage: error.message || error.statusText });
				}
			);
	}

	return (
		<form>
			<h1> Sign In </h1>

			<label htmlFor="email">
				E-Mail
				<input
					type="email" placeholder="E-Mail"
					id="email" name="email" onChange={handleDataChange}
				/>
			</label>

			<label htmlFor="password">
				Password
				<input
					type="password" placeholder="Password"
					id="password" name="password" onChange={handleDataChange}
				/>
			</label>

			{/* display error message if present */}
			{
				data.errorMessage &&  (<span>{data.errorMessage}</span>)
			}

			<button onClick={handleSubmit} disabled={data.isSubmitting}>
				{ data.isSubmitting ? 'Logging in...' : 'Log In' }
			</button>
			<Link href="/app/register">No account yet? Register here!</Link>
		</form>
	);
};

export default Login;
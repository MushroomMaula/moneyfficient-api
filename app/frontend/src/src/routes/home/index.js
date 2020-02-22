import { h } from 'preact';
import { useContext } from 'preact/compat';
import { AuthContext } from '../../index';


const Home = () => {
	const { dispatch } = useContext(AuthContext);
	function logout () {
		dispatch({ type: 'logout', payload: {} });
	}
	return (
		<div style="text-align: center;">
			<p>You are on the Homepage</p>
			<button
				onClick={logout}
			> Logout
			</button>
		</div>
	);
};

export default Home;

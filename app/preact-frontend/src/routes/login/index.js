import { h, Component } from 'preact';
import style from './style';


export default class Login extends Component {
	render() {
		return (
			<div class={style.card}>
				<h1> Login </h1>
				<form>
					<label>Email:</label>
					<input type={'text'} />
				</form>
			</div>
		);
	}
}

import { h, Component } from 'preact';
import ExpenseList from '../../components/ExpenseList';


export default class Home extends Component{
	render(props, state, context) {
		return (
			<div>
				<h1> Home </h1>
				<ExpenseList />
			</div>
		);
	}
}

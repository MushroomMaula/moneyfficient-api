import { h, Component } from 'preact';


export default class ExpenseList extends Component {
	fetchExpenses = () => null;

	render(props, state, context) {
		return (
			<div>
				<label> List of expenses</label>
			</div>
		);
	}
}

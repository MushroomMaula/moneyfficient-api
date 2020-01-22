import { h, Component } from 'preact';


export  default class ExpenseCard extends Component{
	constructor (value, date, category) {
		super();
		this.state.value = value;
		this.state.date = date;
		this.state.category = category;
	}

	render(props, state, context) {
		return (
			<div class="card">
				<label>{this.state.date}</label>
				<label>{this.state.value}</label>
				<label>{this.state.category}</label>
			</div>
		);
	}
}
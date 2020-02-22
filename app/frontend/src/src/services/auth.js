class API {
	constructor (baseUrl) {
		if (baseUrl.charAt(baseUrl.length - 1) !== '/') {
			baseUrl += '/';
		}
		this.baseUrl = baseUrl;
	}

	async makeRequest (endpoint='', method='GET', bodyParams=null) {
		const response = await fetch(
			this.baseUrl+endpoint,
			{
				method: method,
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				body: bodyParams
			}
		);
		return await response.json();
	}
}


class TestAPI extends API {
	constructor () {
		super(`${document.location.protocol}//${document.location.hostname}:${document.location.port}/`);
		this.counter = 0;
	}

	async login(loginData) {
		// create formdata
		let formData = new FormData();
		formData.append('username', loginData.email);
		formData.append('password', loginData.password);
		console.log(Array.from(formData.entries()));

		// send form data
		const response =  await fetch(
			this.baseUrl + 'auth/login',{
				method: 'POST',
				body: formData
			}
		);
		if (!response.ok) {
			throw new Error("Invalid Credentials");
		} else {
			return await response.json();
		}
	}

	async createUser () {
		this.counter += 1;
		return await this.makeRequest(
			'/users',
			'POST',
			{ id: this.counter, name: `User #${this.counter}`, password: 'fake-pw' }
		);
	}

	async getUserById (id) {
		const data = await this.makeRequest(
			`/users?orderKey=id&filterValue=${id}`
		);
		if (!data.ok) {
			return null;
		}
		return data.result;
	}
}

export const api = new TestAPI();
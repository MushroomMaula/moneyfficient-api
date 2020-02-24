class API {
	constructor (baseUrl) {
		if (baseUrl.charAt(baseUrl.length - 1) !== '/') {
			baseUrl += '/';
		}
		this.baseUrl = baseUrl;
	}

	async makeRequest (endpoint='', method='GET', bodyParams=null) {
		return await fetch(
			this.baseUrl + endpoint,
			{
				method: method,
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				body: bodyParams
			}
		);
	}
}


class TestAPI extends API {
	constructor () {
		super(`${document.location.protocol}//${document.location.hostname}:${document.location.port}/`);
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

	async createUser (registerData) {
		console.log(registerData);
		const response =  await this.makeRequest(
			'user/register',
			'POST',
			JSON.stringify(registerData)
		);
		const data = await response.json();
		if (!response.ok) {
			throw new Error(data.detail);
		} else {
			return data;
		}
	}
}

export const api = new TestAPI();
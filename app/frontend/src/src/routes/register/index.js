import { h } from 'preact';
import {useState} from "preact/hooks";
import { api } from '../../services/auth';
import {useContext} from "preact/compat";
import {AuthContext} from "../../index";

const Register = () => {
  const initialState = {
    email: '',
    username: '',
    password: '',
    isSubmitting: false,
    errorMessage: null
  };
  const [data, setData] = useState(initialState);
  const { dispatch } = useContext(AuthContext);

  function handleDataChange(event) {
    event.preventDefault();
		// use the name property the of the input field to change the data
		setData({ ...data, [event.target.name]: event.target.value });
  }

  function handleSubmit(event) {
    event.preventDefault();
    console.log(data);
    setData({ ...data, isSubmitting: true, errorMessage: null});
    api.createUser({
      email: data.email, username: data.username, password: data.password
    })
      // dispatch successful registration to AuthContext
      .then(
        res => {
          dispatch({
            type: 'login',
            payload: res.login_credentials
          });
        }
      )
      // catch possible Registration Error
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
      <h1> Sign Up</h1>
      <label htmlFor="email">
        E-Mail
        <input
          type="email" name="email"
          placeholder="E-Mail"
          onChange={handleDataChange}
        />

      </label>
      <label htmlFor="username">
        Username
        <input
          type="text" name="username"
          placeholder="username"
          onChange={handleDataChange}
        />
      </label>
      <label htmlFor="password">
        Password
        <input
          type="password" name="password"
          placeholder="password"
          onChange={handleDataChange}
        />
      </label>
      {/* display error message if present */}
			{
				data.errorMessage &&  (<span>{data.errorMessage}</span>)
			}
      <button disabled={data.isSubmitting} onClick={handleSubmit}>
        { data.isSubmitting ? 'Signing Up' : 'Sign Up' }
      </button>
    </form>
  )
};

export default Register;
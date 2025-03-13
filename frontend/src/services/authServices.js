import axios from "axios";
import { getCookie } from "../utils/cookies";

// change later on for production to real URL
const API_URL = process.env.VUE_APP_API_URL;

export async function register(email, username, password) {
    const response = await axios.post(`${API_URL}/village/v1/register`, {
        email,
        username,
        password
    });
    return response.data;
}

export async function signin(identifier, password) {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.post(
        `${API_URL}/village/v1/login`,
        {identifier, password},
        {
            headers: { "X-CSRFToken": csrfToken },
        }
    );
    return response.data;
}

export async function signout() {
    const csrfToken = getCookie("csrftoken");
    const response = await axios.post(
        `${API_URL}/village/v1/logout`,
        {},
        {
            headers: { "X-CSRFToken": csrfToken },
        }
    );
    return response.data;
}


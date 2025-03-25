import apiClient from "../utils/axios.js";

// change later on for production to real URL

export const register = async (email, username, password) => {
    const response = await apiClient.post("/village/v1/register", {
        email,
        username,
        password
    }, {
        timeout: 5000
    });
    return response.data;
}

export const signin = async (identifier, password) =>  {
    const response = await apiClient.post("/village/v1/login",
        {
            identifier,
            password
        }, {
            timeout: 5000
        }
    );
    return response.data;
}

export const signout = async () => {
    const response = await apiClient.post("/village/v1/logout");
    return response.data;
}


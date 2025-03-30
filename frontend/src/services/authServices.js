import apiClient from "../utils/axios.js";

// change later on for production to real URL

export const register = async (email, username, password) => {
    const response = await apiClient.post("/village/v1/register/", {
        email,
        username,
        password
    }, {
        timeout: 5000
    });
    return response.data;
}

export const signin = async (identifier, password) =>  {
    const response = await apiClient.post("/village/v1/login/",
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
    const response = await apiClient.post("/village/v1/logout/");
    return response.data;
}

export const getPersonalVillageMembers = async () => {
    const response = await apiClient.get("/village/v1/personal-village-members/");
    return response.data;
  };
  
  export const listUserVillages = async () => {
    const response = await apiClient.get("/village/v1/list-user-villages/");
    return response.data;
  };
  
  export const getVillageParticipants = async (user) => {
    const response = await apiClient.get(`/village/v1/get-village-participants/${user}/`);
    return response.data;
  };
  
  export const addVillagerToVillage = async (user, villagerId) => {
    const formData = new FormData();
    formData.append("village_id", user);
    formData.append("villager_id", villagerId);
  
    const response = await apiClient.post("/village/v1/add-village/", formData);
    return response.data;
  };
  
  export const removeVillagerFromVillage = async (user, villagerId) => {
    const formData = new FormData();
    formData.append("village_id", user);
    formData.append("villager_id", villagerId);
  
    const response = await apiClient.post(`/village/v1/remove-village/${user}/`, formData);
    return response.data;
  };
  
  export const initializeVillage = async () => {
    const response = await apiClient.post("/village/v1/initialize-village/");
    return response.data;
  };
  
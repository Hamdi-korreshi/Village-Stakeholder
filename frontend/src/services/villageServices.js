import apiClient from "../utils/axios.js";


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

// services/villageServices.js
export const addVillagerToVillage = async (villagerUsername, supportRole) => {
    const response = await apiClient.post(`/village/v1/add-villager/`, {
      villager_username: villagerUsername,
      support_role: supportRole
    });
    return response.data;
  };
  

export const removeVillagerFromVillage = async (user, villagerId) => {
    const formData = new FormData();
    formData.append("village_id", user);
    formData.append("villager_id", villagerId);

    const response = await apiClient.post(`/village/v1/remove-villager/${user}/`);
    return response.data;
};

export const initializeVillage = async (ownerId, description) => {
    const response = await apiClient.post("create-village/", {
        owner: ownerId,
        description: description
    });
    return response.data;
};




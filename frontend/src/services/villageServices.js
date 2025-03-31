import apiClient from "../utils/axios.js";


export const getPersonalVillageMembers = async () => {
    const response = await apiClient.get("get-village-members/");
    return response.data;
  };
  

export const listUserVillages = async () => {
    const response = await apiClient.get("list-user-villages/");
    return response.data;
};

export const getVillageParticipants = async (user) => {
    const response = await apiClient.get(`get-village-participants/${user}/`);
    return response.data;
};

// services/villageServices.js
export const addVillagerToVillage = async (villagerUsername, supportRole) => {
    const response = await apiClient.post(`add-villager/`, {
      villager_username: villagerUsername,
      support_role: supportRole
    });
    return response.data;
  };
  

export const removeVillagerFromVillage = async (villagerUsername) => {
    const response = await apiClient.post("remove-villager/", {
      villager_username: villagerUsername,
    });
    return response.data;
  };
  
  
  

export const initializeVillage = async (description) => {
  const response = await apiClient.post("initialize-village/", {
    description: description,
  });
  return response.data;
};





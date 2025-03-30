import apiClient from "../utils/axios.js";

export const get_my_village = async (user_id) => {
    const response = await apiClient.post("/village/v1/personal-village-members/",
        {
            user_id
        },{
            timeout: 5000
        }
    );
    return response.data;
}
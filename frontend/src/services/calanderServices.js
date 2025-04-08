import apiClient from "../utils/axios.js";

export const getNotifications = async () => {
    const response = await apiClient.get("get-notifications/");
    return response.data;
  }
//TODO: make parameters for all information being passed to create event 
export const makeCalendarEvent = async () => {
    const response = await apiClient.post("create-calendar-event/");
    return response.data;
  };


//TODO: make 
export const makeCalendarResposne = async (inviteeResponse) => {
    const response = await apiClient.post("create-calendar-response/",{
        invitee_response: inviteeResponse,
    });
    return response.data;
  };
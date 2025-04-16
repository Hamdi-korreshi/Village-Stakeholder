import apiClient from "../utils/axios.js";

// ======== Calendar Data Retrieval ========

// 1. Get calendar events for the current user
export const getCalendarEvents = async () => {
  const response = await apiClient.get("get-calendar-events/");
  return response.data;
};

// 2. Get notifications for the current user
export const getNotifications = async () => {
  const response = await apiClient.get("get-notification/");
  return response.data;
};

// ======== Calendar Event Management ========

// 3. Create a new calendar event
export const makeCalendarEvent = async (eventData) => {
  const response = await apiClient.post("create-calendar-event/", eventData);
  return response.data;
};

// 4. Update an existing calendar event
export const updateCalendarEvent = async (eventData) => {
  const response = await apiClient.post("update-calendar-event/", eventData);
  return response.data;
};

// 5. Delete a calendar event
export const deleteCalendarEvent = async (eventId) => {
  const response = await apiClient.post("delete-calendar-event/", {
    event_id: eventId,
  });
  return response.data;
};

// ======== Calendar Invite Management ========

// 6. Send calendar invites to multiple users
export const sendCalendarInvites = async (eventId, inviteeUsernames) => {
  const response = await apiClient.post("calendar-invite-create/", {
    event_id: eventId,
    invitees: inviteeUsernames,
  });
  return response.data;
};

// 7. Respond to an invite (accept or decline)
export const respondToCalendarInvite = async (inviteId, responseStatus) => {
  const response = await apiClient.post("calendar-invite-accept/", {
    invite_id: inviteId,
    response: responseStatus, // "accepted" or "declined"
  });
  return response.data;
};

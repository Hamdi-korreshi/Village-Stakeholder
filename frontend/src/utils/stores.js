import { defineStore } from 'pinia';

export const store_user_info = defineStore('user', {
    state: () => ({
        user: null,
    }),
    actions: {
        set_user(userData) {
            this.user = userData;
            console.log("bruh",userData);
        },
        clear_user() {
            this.user = null;
        },
    },
    persist: true,
} );

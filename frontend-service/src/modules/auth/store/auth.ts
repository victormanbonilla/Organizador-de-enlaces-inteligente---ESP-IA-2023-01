import { defineStore } from 'pinia';

interface AuthState {
  status: string;
  user: User;
  errorMessage: string | undefined;
}

interface UserData {
  name: string;
  token: string;
}

export type User = UserData | {};

const authStore = defineStore('auth', {
  state: (): AuthState => ({
    status: 'checking',
    user: {},
    errorMessage: undefined,
  }),
  actions: {
    onChecking() {
      this.status = 'checking';
      this.user = {};
      this.errorMessage = undefined;
    },
    onLogin(payload: User = {}) {
      this.status = 'authenticated';
      this.user = payload;
      this.errorMessage = undefined;
    },
    onLogout(payload: string) {
      this.status = 'not-authenticated';
      this.user = {};
      this.errorMessage = payload;
    },
    clearErrorMessage() {
      this.errorMessage = undefined;
      this.user = {};
    },
  },
});

export { authStore };

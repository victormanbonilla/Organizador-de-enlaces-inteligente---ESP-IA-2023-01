import { router } from './../../../router';
import { storeToRefs } from 'pinia';
import { authStore } from '../store/auth';
import { http } from '../../../environments/environment.prod';
import jwtDecode from 'jwt-decode';

interface TokenFields {
  user: string;
  route: string;
  exp: number;
}

const useAuthStore = () => {
  const baseUrl = '/auth';
  const store = authStore();
  const { errorMessage, status, user } = storeToRefs(store);

  const startLogin = async (user: string, password: string) => {
    const url = `${baseUrl}/login`;
    store.onChecking();

    try {
      const { data } = await http.post<{ token: string }>(url, {
        user,
        password,
      });
      if (!data.token) return;

      const decoded = jwtDecode<TokenFields>(data.token);
      store.onLogin({ name: decoded.user, token: data.token });
      router.push('/admin/home');
    } catch (error) {
      store.onLogout('Credenciales incorrectas');
      setTimeout(() => {
        store.clearErrorMessage();
      });
    }
  };

  const startRegister = async (user: string, password: string) => {
    const url = `${baseUrl}/register`;
    const body = { user, password };
    store.onChecking();

    try {
      const { data } = await http.post<{ success: boolean }>(url, body);
      if (!data.success) return false;
      startLogin(user, password);
      return true;
    } catch (error) {
      store.onLogout('error when resgistering the user');
      setTimeout(() => {
        store.clearErrorMessage();
      });
      return false;
    }
  };

  const startLogout = () => {
    store.onLogout('');
    router.push('/auth/login');
  };

  return {
    // Properties
    errorMessage,
    status,
    user,

    // Methods
    // checkAuthToken,
    startRegister,
    startLogout,
    startLogin,
  };
};

export { useAuthStore };

// const checkAuthToken = async () => {
//   const url = `${baseUrl}/`;
//   const store = authStore();
//   const { user } = storeToRefs(store);

//   if (!user.value) return store.onLogout('');
//   const rawUser = { ...user.value };

//   try {
//     const { data } = await http.post<{ ok: boolean }>(url, {
//       token: rawUser.token,
//     });
//     const decoded = jwtDecode<TokenFields>(data.token);
//     store.onLogin({ name: decoded.user, token: data.token });
//   } catch (error) {
//     localStorage.clear();
//     store.onLogout('');
//   }
// };

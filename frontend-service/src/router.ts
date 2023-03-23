import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from 'vue-router';
import { adminRoutes } from './modules/admin/routes';
import { useAuthStore } from './modules/auth/composables/useAuthStore';
import { authRoutes } from './modules/auth/routes';
import { publicRoutes } from './modules/shared/routes';

const routes: RouteRecordRaw[] = [
  { ...publicRoutes },
  { ...adminRoutes },
  { ...authRoutes },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _, next) => {
  if (to.matched[0].path !== '/admin') {
    next();
    return;
  }

  const { user } = useAuthStore();
  const rawUser = { ...user.value };

  rawUser.token !== undefined ? next() : router.push('/auth/login');
});

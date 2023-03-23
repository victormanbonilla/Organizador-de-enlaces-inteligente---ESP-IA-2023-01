import type { RouteRecordRaw } from 'vue-router';
import LoginView from './views/LoginView.vue';
import RegisterView from './views/RegisterView.vue';

const authRoutes: RouteRecordRaw = {
    path: '/auth',
    component: () => import('./views/LayoutView.vue'),
    children: [
        { path: '', redirect: '/login' },
        { path: 'login', component: LoginView },
        { path: 'register', component: RegisterView },
        { path: '/:pathMatch(.*)*', redirect: '/auth/login' },
    ],
}

export { authRoutes };

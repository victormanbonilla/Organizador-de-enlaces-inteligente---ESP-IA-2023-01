import type { RouteRecordRaw } from 'vue-router';

import HomeView from './views/HomeView.vue';
import SettingsView from './views/SettingsView.vue';
import AnalyticsView from './views/AnalyticsView.vue';

const adminRoutes: RouteRecordRaw = {
  path: '/admin',
  component: () => import('./views/LayoutView.vue'),
  children: [
    { path: '', redirect: '/admin/home' },
    { path: 'home', component: HomeView },
    { path: 'analytics', component: AnalyticsView },
    { path: 'settings', component: SettingsView },
  ],
};

export { adminRoutes };

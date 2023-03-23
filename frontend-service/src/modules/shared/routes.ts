import type { RouteRecordRaw } from 'vue-router';
import PublicView from './views/PublicView.vue';

const publicRoutes: RouteRecordRaw = {
    path: '/public/:id',
    component: PublicView
};

export { publicRoutes };

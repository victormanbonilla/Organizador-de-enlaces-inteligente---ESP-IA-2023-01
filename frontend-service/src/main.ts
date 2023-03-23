import { router } from './router';
import { createApp } from 'vue';
import './style.css';
import 'element-plus/dist/index.css';
import App from './App.vue';
import { createPinia } from 'pinia';

createApp(App)
    .use(createPinia())
    .use(router)
    .mount('#app');

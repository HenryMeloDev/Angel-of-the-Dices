import './assets/main.css';

import { createApp } from 'vue';
import "./styles/global.css";
import App from './App.vue';
 // @ts-ignore
import router from '../src/router/router.js';

const app = createApp(App)
app.use(router)
app.mount('#app')

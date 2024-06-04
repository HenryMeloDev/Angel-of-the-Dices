import { createWebHistory, createRouter } from "vue-router";

import Home from "../screens/Home.vue";
import Sheets from "../screens/Sheets.vue"
import CreateSheet from "../screens/CreateSheet.vue"

const routes = [
    { path: "/", component: Home },
    { path: "/sheets", component: Sheets},
    { path: "/sheets/new", component: CreateSheet},
  ];

  const router = createRouter({
    history: createWebHistory(),
    routes,
  });

  export default router;
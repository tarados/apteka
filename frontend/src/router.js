import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            meta: {layout: 'MainLayout'},
            component: () => import('./templates/Home.vue')
        },
        {
            path: '/maps',
            name: 'maps',
            meta: {layout: 'MainLayout'},
            component: () => import('./templates/Maps.vue')
        }

    ]
})

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
            params: {textseach: 'ddd'},
            component: () => import('./templates/Home.vue')
        },
        {
            path: '/basket/checkout/maps',
            name: 'maps',
            meta: {layout: 'EmptyLayout'},
            component: () => import('./templates/Maps.vue')
        },
        {
            path: '/product',
            name: 'product',
            meta: {layout: 'MainLayout'},
            component: () => import('./templates/Products.vue')
        },
        {
            path: '/product/:textseach',
            name: 'productseach',
            meta: {layout: 'MainLayout'},
            component: () => import('./templates/Products.vue')
        },
        {
            path: '/basket',
            name: 'basket',
            meta: {layout: 'EmptyLayout'},
            component: () => import('./templates/Basket')
        },
        {
            path: '/basket/checkout',
            name: 'checkout',
            meta: {layout: 'EmptyLayout'},
            component: () => import('./templates/Checkout')
        }

    ]
})

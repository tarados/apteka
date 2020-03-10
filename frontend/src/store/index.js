import Vue from 'vue';
import Vuex from 'vuex';
import basketStore from "./modules/basketStore";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        basketStore
    }
})


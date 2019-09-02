<template>
    <div class="container-fluid">
        <b-navbar toggleable="lg" class="navbar fixed-top">
            <b-navbar-brand href="#">
                <img src="../brand.png" alt="Kitten">
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item href="#">Link</b-nav-item>
                    <b-nav-item href="#" disabled>Disabled</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <component v-bind:is="currentPage" v-if="currentPage"></component>
    </div>
</template>

<script>
    import maps from "./Maps";
    import Product from "./Product";

    export default {
        name: "StartScreen",

        components: {
            maps,
            Product
        },

        data() {
            return {
                currentPage: "Product"
            }
        }
    }
</script>

<style scoped>


    #nav-collapse {
        padding-top: 13px;
    }

    .navbar {
        border-bottom: 1px solid #ced4da;
    }
</style>

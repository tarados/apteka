<template>
    <div>
        <Products/>
    </div>
</template>

<script>
    import Products from "./Products";

       export default {
        name: "Home",
        components: {
            Products
        },
        mounted() {
            this.$store.commit("addProductsFromBasket");
        }
       }
</script>

<style scoped>

</style>
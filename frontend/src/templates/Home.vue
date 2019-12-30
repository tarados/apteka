<template>
    <div>
        <NavBar/>
        <Products/>
    </div>
</template>

<script>
    import Products from "./Products";
    import NavBar from "./Navbar";
       export default {
        name: "Home",
        components: {
            Products,
            NavBar
        }
    }
</script>

<style scoped>

</style>
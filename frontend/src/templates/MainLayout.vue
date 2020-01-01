<template>
    <div>
        <NavBar/>
        <slot/>
    </div>
</template>

<script>
    import NavBar from "./Navbar";
    export default {
        components: {
            NavBar
        }

    }
</script>

<style scoped>

</style>

<template>
    <div>
        <Navbar />
        <slot/>
    </div>
</template>

<script>
    import Navbar from "./Navbar";

    export default {
        components: {
            // eslint-disable-next-line vue/no-unused-components
            Navbar
        }
    }
</script>

<style scoped>

</style>

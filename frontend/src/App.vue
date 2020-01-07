<template>
    <div id="app">
        <component :is="layout">
            <router-view/>
        </component>
    </div>
</template>

<script>
    import EmptyLayout from './templates/EmptyLayout'
    import MainLayout from './templates/MainLayout'

    export default {
        computed: {
            layout() {
                return this.$route.meta.layout
            }
        },
        components: {
            EmptyLayout, MainLayout
        }
    }
</script>


<style scoped>

</style>

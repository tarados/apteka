<template>
    <div class="productStorage">
        <app-poduct v-if="state == 'product'"></app-poduct>
        <app-farmacy v-else-if="state == 'farmacy'"></app-farmacy>
        <app-maps v-else-if="state == 'maps'"></app-maps>
        <div v-else>Unknown state</div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                state: 'farmacy'
            }
        }
    }
</script>

<style scoped>

</style>

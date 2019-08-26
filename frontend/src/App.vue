<template>
    <div class="productStorage">
        <app-startscreen v-if="state === 'start'"></app-startscreen>
        <app-poduct v-else-if="state === 'product'"></app-poduct>
        <app-farmacy v-else-if="state === 'farmacy'"></app-farmacy>
        <app-maps v-else-if="state === 'maps'"></app-maps>
        <div v-else>Unknown state</div>
    </div>

</template>

<script>

    export default {
        data() {
            return {
                state: 'start'
            }
        }
    }
</script>

<style scoped>

</style>

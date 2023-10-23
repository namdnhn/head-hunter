<template>
    <main class="pt-16 lg:pt-20 w-full h-auto">
        <sidebar></sidebar>
    </main>
</template>

<script lang="ts">
    import SideBar from '../../components/sidebar/SideBar.vue'
    export default {
        components: {
            sidebar: SideBar,
        }
    }
</script>

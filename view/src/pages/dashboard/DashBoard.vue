<template>
    <main class="pt-16 lg:pt-20 w-full h-auto">
        <sidebar></sidebar>
        <MiniHeaderCard></MiniHeaderCard>
    </main>
</template>

<script lang="ts">
    import SideBar from '../../components/sidebar/SideBar.vue'
    import MiniHeaderCard from '../../components/sidebar/MiniHeaderCard.vue';
    export default {
        components: {
            sidebar: SideBar,
            MiniHeaderCard: MiniHeaderCard
        }
    }
</script>

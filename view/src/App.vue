<template>
    <the-header></the-header>
    <router-view v-slot="slotProps">
        <transition name="route" mode="out-in">
            <component :is="slotProps.Component"></component>
        </transition>
    </router-view>
    <the-footer></the-footer>
</template>

<script lang="ts">
import TheHeader from "../src/components/layouts/TheHeader.vue";
import TheFooter from "../src/components/layouts/TheFooter.vue";
export default {
    components: { TheHeader, TheFooter },
    created() {
        this.$store.dispatch('autoLogin')
    },
    computed: {
        didAutoLogout() {
            return this.$store.getters.didAutoLogout
        }
    },
    watch: {
        didAutoLogout(curValue, newValue) {
            if (curValue && curValue !== newValue) {
                this.$router.replace('/homepage')
            }
        }
    }
};
</script>

<style>
.route-enter-from {
    opacity: 0;
    transform: translateY(-30px);
}

.route-leave-to {
    opacity: 0;
    transform: translateY(30px);
}

.route-enter-to,
.route-leave-from {
    opacity: 1;
    transform: translateY(0);
}

.route-enter-active {
    transition: all 0.3s ease-out;
}

.route-leave-active {
    transition: all 0.3s ease-in;
}
</style>

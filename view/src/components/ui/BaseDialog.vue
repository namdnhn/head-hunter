<template>
    <teleport to="body">
        <div class="fixed top-0 left-0 w-full h-screen z-10 backdrop"></div>
    </teleport>
    <transition name="dialog">
        <dialog open>
            
        </dialog>
    </transition>
</template>

<style scoped>
    .backdrop {
        background-color: rgba(0, 0, 0, 0.75);
    }
</style>
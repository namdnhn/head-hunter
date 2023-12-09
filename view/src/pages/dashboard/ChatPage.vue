<template>
	<main
		class="fixed top-0 left-0 right-0 w-full h-full bg-white pt-16 lg:pt-20 flex"
	>
		<!-- list chat user  -->
		<div
			class="basis-1/4 border border-e-2 overflow-y-scroll overflow-x-hidden p-2 flex flex-col gap-2"
		>
			<user-chatted
				v-for="receiver in receivers"
				:user_id="receiver.id"
				:fullname="receiver.fullname"
			></user-chatted>
		</div>
		<!-- chat box  -->
		<router-view v-slot="slotProps">
			<transition name="route" mode="out-in">
				<component :is="slotProps.Component"></component>
			</transition>
		</router-view>
	</main>
</template>

<script lang="ts">
import UserChatted from "../../components/message/UserChatted.vue";
export default {
	components: {
		UserChatted
	},
	data() {
		return {
			receiver: "",
			receivers: [{
				id: 0,
				fullname: ""
			}],
		};
	},
	mounted() {
		this.$nextTick(function () {
			const chatContainer = this.$refs.chatContainer as HTMLDivElement;
			chatContainer.scrollTop = chatContainer.scrollHeight;
		});

		this.getConversation();
	},
	methods: {
		async getConversation() {
			const user_id = this.$store.getters.userId;
			const response = await fetch(
				`http://localhost:8000/api/chat/members/${user_id}`,
				{
					method: "GET",
					headers: {
						"Content-Type": "application/json",
					},
				}
			);

			const data = await response.json();
			this.receivers = data;
		}
	},
};
</script>

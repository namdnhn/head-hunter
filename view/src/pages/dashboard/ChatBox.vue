<template>
	<div class="basis-3/4 relative">
		<!-- header chat box  -->
		<div
			class="absolute w-full left-0 right-0 top-0 py-2 px-4 flex gap-4 items-center border border-e-2 shadow h-16"
		>
			<img
				src="https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF"
				alt="avt"
				class="h-12 w-12 rounded-full"
			/>
			<h2 class="lg:text-lg md:text-base text-sm font-bold text-sky-900">
				{{ fullname }}
			</h2>
		</div>

		<div
			ref="chatContainer"
			class="absolute top-16 bottom-16 w-full py-2 px-4 overflow-y-scroll flex flex-col gap-2"
		>
			<message-card
				v-for="message in messages"
				:key="message.id"
				:avt="message.avt"
				:type="message.sender_id"
				:content="message.content"
				:time="message.timestamp"
			></message-card>
		</div>

		<!-- input message  -->
		<div
			class="absolute w-full left-0 right-0 bottom-0 py-2 px-4 flex items-center gap-4 border border-t-2 shadow h-16"
		>
			<input
				v-model="newMessage"
				type="text"
				class="p-2 bg-slate-200 w-full rounded-3xl lg:text-base md:text-sm text-xs"
				placeholder="Aa"
			/>
			<button
				@click="sendMessage"
				class="p-2 bg-green-300 rounded-lg text-green-800 hover:cursor-pointer hover:bg-green-400 hover:text-green-900"
			>
				Gửi
			</button>
		</div>
	</div>
</template>

<script lang="ts">
import MessageCard from "../../components/message/MessageCard.vue";
export default {
	components: {
		MessageCard,
	},
	props: ["id"],
	data() {
		return {
			messages: [
				{ id: 0, avt: "", sender_id: "", content: "", timestamp: "" },
			],
			fullname: "",
			newMessage: "",
			conv_id: 0,
		};
	},
	mounted() {
		this.$nextTick(function () {
			const chatContainer = this.$refs.chatContainer as HTMLDivElement;
			chatContainer.scrollTop = chatContainer.scrollHeight;
		});

		this.getFullname();
		this.getMessage();
	},
	methods: {
		async getFullname() {
			const receiver_id = this.id;
			const getUser = await fetch(
				`http://localhost:8000/api/user/${receiver_id}`
			);
			const temp = await getUser.json();
			console.log(temp.fullname);
			this.fullname = temp.fullname;
		},
		async getMessage() {
			const user_id = localStorage.getItem("userId");
			const receiver_id = this.id;
			const getConversationId = await fetch(
				`http://localhost:8000/api/chat/conversation/${user_id}/${receiver_id}`
			);
			const conv_id = await getConversationId.json();
			this.conv_id = conv_id;
			const response = await fetch(
				`http://localhost:8000/api/chat/messages/${conv_id}`,
				{
					method: "GET",
					headers: {
						"Content-Type": "application/json",
					},
				}
			);
			const data = await response.json();
			this.messages = data;
			console.log(data);
		},
		async sendMessage() {
			const sender_id = localStorage.getItem("userId");
			const conversation = this.conv_id;
			const newMessage = this.newMessage;
			try {
				await fetch(`http://localhost:8000/api/chat/message`, {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({
						sender_id: Number(sender_id),
						conversation_id: Number(conversation),
						content: newMessage,
					}),
				});
				this.newMessage = "";
			} catch (error) {
				console.error("Error sending message", error);
			}
		},
	},
	watch: {
		id: function (newId, oldId) {
			if (newId !== oldId) {
				this.getMessage();
				this.getFullname();
			}
		},
	},
};
</script>

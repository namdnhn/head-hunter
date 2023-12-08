<template>
	<router-link
		:to="getRouterLink"
		class="w-full bg-slate-100 hover:bg-sky-100 hover:cursor-pointer p-2 rounded-lg flex justify-between items-center"
	>
		<div class="flex gap-2 items-center">
			<img
				src="https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF"
				alt="avt"
				class="h-14 w-14 rounded-full"
			/>
			<div>
				<h2
					class="lg:text-base md:text-sm text-xs font-bold text-sky-900"
				>
					{{ fullname }}
				</h2>
				<p class="lg:text-sm text-xs text-slate-500">
					{{ lastMessage.content }}
				</p>
			</div>
		</div>
		<p class="lg:text-sm text-xs text-slate-500">
			{{ formattedTimestamp }}
		</p>
	</router-link>
</template>

<script lang="ts">
import { getLastMessage } from "../../../services/message";
import { getDatabase, ref, onValue } from "firebase/database";
export default {
	data() {
		return {
			conv_id: 0,
			lastMessage: { content: "", timestamp: 0 },
		};
	},
	props: ["fullname", "user_id"],
	computed: {
		getRouterLink(): string {
			return `/chat/${this.user_id}`;
		},
		formattedTimestamp(): string {
			// Chuyển đổi timestamp thành dạng giờ đọc được ở đây
			const date = new Date(this.lastMessage.timestamp); // Nhân 1000 để chuyển đổi từ giây sang mili giây
			// const hours = date.getHours();
			// const minutes = "0" + date.getMinutes();
			// const seconds = "0" + date.getSeconds();
			// const formattedTime =
			// 	hours + ":" + minutes.substr(-2) + ":" + seconds.substr(-2);
			return date.toLocaleString('en-GB');
		},
	},
	mounted() {
		console.log("UserId: ", this.user_id);
		if (this.user_id > 0) this.getConversationId();
		if (this.conv_id > 0) this.getLastMessage();
	},
	methods: {
		async getConversationId() {
			console.log("Thực hiện");
			const user_id = localStorage.getItem("userId");
			const receiver_id = this.user_id;
			const getConversationId = await fetch(
				`http://localhost:8000/api/chat/conversation/${user_id}/${receiver_id}`
			);
			const conv_id = await getConversationId.json();
			this.conv_id = conv_id;
			console.log("conv_id: ", this.conv_id);
		},
		async getLastMessage() {
			const message = await getLastMessage(this.conv_id);
			if (message !== null) {
				this.lastMessage = message;
				console.log("Đây nè", this.lastMessage);
			} else {
				console.log("Không có tin nhắn cuối cùng");
			}

			const messagesRef = ref(
				getDatabase(),
				`conversations/${this.conv_id}/messages`
			);

			onValue(messagesRef, async () => {
				const message = await getLastMessage(this.conv_id);
				if (message !== null) {
					this.lastMessage = message;
				}
			});
		},
	},
	watch: {
		user_id(newUserId, oldUserId) {
			if (newUserId !== oldUserId) {
				this.getConversationId();
			}
		},
		conv_id(newConverId, oldConverId) {
			if (newConverId !== oldConverId) {
				this.getLastMessage();
			}
		},
	},
};
</script>

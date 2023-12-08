import { ref, get, query, orderByChild, limitToLast } from "firebase/database";
import { database } from "./app";

export async function getLastMessage(conversationId: number) {
    console.log("Bat dau nao")
	const messagesRef = ref(
		database,
		`conversations/${conversationId}/messages`
	);
	const messagesQuery = query(
		messagesRef,
		orderByChild("timestamp"),
		limitToLast(1)
	);
    console.log("kết quả truy vấn: ", messagesQuery);

	try {
		const messageSnapshot = await get(messagesQuery);

		if (messageSnapshot.exists()) {
			const lastMessage = messageSnapshot.val();
            const values = Object.values(lastMessage);
            console.log("last message: ", values);
			return values[0];
		}

		return null;
	} catch (error) {
		console.error("Error getting last message", error);
		return null;
	}
}

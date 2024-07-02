const { Client } = require("@notionhq/client")
NOTION_TOKEN = "secret_o1hLhegKc6iIS7ZZdP0EhDfXn6XW24QL5u09lswDS2l"
DATABASE_ID = "ce17339287144dfdbcbf15d391ec5e96"

// Initializing a client
const notion = new Client({
	auth: process.env.NOTION_TOKEN,
})

const getUsers = async () => {
	const listUsersResponse = await notion.users.list({})
}
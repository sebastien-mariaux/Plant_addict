import { Application } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"
import messagesController from "./messages_controller.js"

window.Stimulus = Application.start()
Stimulus.register("messages", messagesController)


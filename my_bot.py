from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7284156733:AAHUpfjB65s7C-ciuHZP8eEM_BgId4-yGTA'

# Define the start command handler
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("البيوت المتاحة", callback_data='available_houses')],
        [InlineKeyboardButton("الشقق المتاحة", callback_data='available_apartments')],
        [InlineKeyboardButton("معلومات الاتصال", callback_data='contact_info')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "مرحباً! أنا بوت تأجير البيوت. كيف يمكنني مساعدتك اليوم؟\n"
        "اختر من الخيارات التالية:",
        reply_markup=reply_markup
    )

# Define callback handler for the options
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'available_houses':
        keyboard = [
            [InlineKeyboardButton("غرفة مزدوجة كبيرة في الكرادة", callback_data='house_1')],
            [InlineKeyboardButton("شقة مكونة من غرفتين في حي هارثيا", callback_data='house_2')],
            [InlineKeyboardButton("ملاذ مركزي مريح في بغداد", callback_data='house_3')],
            [InlineKeyboardButton("استوديو ساحر في قلب بغداد", callback_data='house_4')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "هنا قائمة بالبيوت المتاحة:\n"
            "اختر من الخيارات أدناه لمزيد من التفاصيل:",
            reply_markup=reply_markup
        )

    elif query.data == 'available_apartments':
        # Similar implementation for apartments if needed
        pass

    elif query.data == 'contact_info':
        await query.edit_message_text(
            "للتواصل معنا:\n"
            "رقم الهاتف: 123-456-7890\n"
            "البريد الإلكتروني: info@example.com\n"
            "سعيدون بخدمتك!"
        )

    elif query.data == 'house_1':
        media = InputMediaPhoto(
            media='https://www.example.com/image_for_house_1.jpg',  # Replace with actual image URL
            caption="غرفة مزدوجة كبيرة في الكرادة - للإناث فقط\n"
                    "   [رابط للعرض](https://www.airbnb.com/rooms/956632535718113571?adults=1&category_tag=Tag%3A8678&children=0&enable_m3_private_room=true&infants=0&pets=0&photo_id=1748983784&search_mode=regular_search&check_in=2024-08-08&check_out=2024-08-13&source_impression_id=p3_1723045625_P3CtlExVGRC3c7tz&previous_page_section_name=1000&federated_search_id=c3cd8829-4d26-4975-867a-a0b388dc52ef)\n"
        )
        await query.message.reply_media_group([media])

    elif query.data == 'house_2':
        media = InputMediaPhoto(
            media='https://www.example.com/image_for_house_2.jpg',  # Replace with actual image URL
            caption="شقة مكونة من غرفتين في حي هارثيا\n"
                    "   [رابط للعرض](https://www.airbnb.com/rooms/1142760834094614193?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&search_mode=regular_search&check_in=2024-08-12&check_out=2024-08-17&source_impression_id=p3_1723045670_P3tSqtvKdvpye_vW&previous_page_section_name=1000&federated_search_id=c3cd8829-4d26-4975-867a-a0b388dc52ef)\n"
        )
        await query.message.reply_media_group([media])

    elif query.data == 'house_3':
        media = InputMediaPhoto(
            media='https://www.example.com/image_for_house_3.jpg',  # Replace with actual image URL
            caption="ملاذ مركزي مريح في بغداد\n"
                    "   [رابط للعرض](https://www.airbnb.com/rooms/1189889349974317079?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&search_mode=regular_search&check_in=2024-08-07&check_out=2024-08-12&source_impression_id=p3_1723045670_P3lxilBkdIG1bVBR&previous_page_section_name=1000&federated_search_id=c3cd8829-4d26-4975-867a-a0b388dc52ef)\n"
        )
        await query.message.reply_media_group([media])

    elif query.data == 'house_4':
        media = InputMediaPhoto(
            media='https://www.example.com/image_for_house_4.jpg',  # Replace with actual image URL
            caption="استوديو ساحر في قلب بغداد - شارع كندي\n"
                    "   [رابط للعرض](https://www.airbnb.com/rooms/1155788629783602465?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&search_mode=regular_search&check_in=2024-08-09&check_out=2024-08-14&source_impression_id=p3_1723045670_P3pKZEpAb1R4qXkt&previous_page_section_name=1000&federated_search_id=c3cd8829-4d26-4975-867a-a0b388dc52ef)\n"
        )
        await query.message.reply_media_group([media])

def main() -> None:
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()

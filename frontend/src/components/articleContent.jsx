import Font from "react-font"
export default function ArticleContent({
    response
}) {

    return (
        <div className="my-2">
            <div className="flex flex-row gap-x-10 py-3">
                <img src={response.message.image} className="max-h-80"/>
                <div className="flex justify-center font-bold text-[60px] text-amber-950">
                    <Font family="Playfair Display">{response.message.curated_articles.data.title}</Font>
                </div> 
            </div>
            <div className="flex justify-center text-[24px] text-amber-950 mt-20">
            <Font family="Lora">{response.message.curated_articles.data.article}</Font>
            </div>
        </div>
    )
}
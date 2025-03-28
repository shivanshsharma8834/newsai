import Font from "react-font"
export default function ArticleContent({
    response
}) {
    return (
        <div>
            <div className="flex flex-row px-20 gap-x-10">
                <img src={response.message.image} className="w-40 h-40"/>
                <div className="flex justify-center font-bold text-[35px]">
                    <Font family="Bodoni-Moda">{response.message.curated_articles.data.title}</Font>
                </div> 
            </div>
            <div className="flex justify-center text-[18px] px-20 mt-3">
            <Font family="Bodoni-Moda">{response.message.curated_articles.data.article}</Font>
            </div>
        </div>
    )
}
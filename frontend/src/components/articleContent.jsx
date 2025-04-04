import Font from "react-font"
export default function ArticleContent({
    response
}) {

    return (
        <div className="my-2">
            {/* Article Image */}
            <div className="flex flex-row gap-x-10 py-3">
                <img src={response.message.image} className="max-h-80 rounded-2xl"/>
                {/* Article Title */}
                <div className="flex justify-center font-bold text-[60px] text-amber-950">
                    <Font family="Playfair Display"><p>{response.message.curated_articles.data.title}</p></Font>
                </div> 
            </div>
            {/* Article Content */}
            <div className="flex justify-center text-[24px] text-amber-950 mt-20">
            <Font family="Lora">{response.message.curated_articles.data.article}</Font>
            </div>
            {/* Article References */}
            <div className="mt-10">
                <Font family="Playfair Display">
                    <h1 className="mb-10 text-2xl font-semibold text-amber-900">References:</h1>
                    <ul className="flex flex-col gap-y-3 text-[20px]">
                    {response.message.sources.map((link, index) => (
                        <li><a key={index} href={`${link}`}>{link}</a></li>
                    ))}
                    </ul> 
                </Font>     
            </div>
        </div>
    )
}
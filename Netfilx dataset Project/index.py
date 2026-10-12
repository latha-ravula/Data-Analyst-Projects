import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_dataset_500.csv')
# df=df.dropna(subset=['Show_ID','Type','Release_Year','Country','Rating','Duration','Genre'])
# type_count=df['Type'].value_counts()  # it counts unique values
# plt.figure(figsize=(6,4))
# plt.bar(type_count.index,type_count.values,color=['skyblue','orange'])
# plt.title("Number of movies VS TV shows on netflix")
# plt.xlabel("Type")
# plt.ylabel('Count')
# plt.tight_layout()
# plt.savefig('movie_vs_tvshows.png')
# plt.show()

# Rating
# rating_counts=df['Rating'].value_counts()
# plt.figure(figsize=(8,6))
# plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
# plt.title("Percentage of Content Rating")


# plt.tight_layout()
# plt.savefig('content_pie.png')
# plt.show()
# Movie Vs Duration

# movie_df=df[df['Type']=='Movie'].copy()
# movie_df['Duration_int']=movie_df['Duration'].str.replace('min','').astype(int)
# plt.figure(figsize=(8,6))
# plt.hist(movie_df['Duration_int'],bins=30,color='purple',edgecolor='black') # bins->commonly used in histogram to control how data is grouped into intervals.
# plt.title('Distrubution of Movie Duration')
# plt.xlabel('Duration (Minutes)')
# plt.ylabel('Number of Movies')
# plt.tight_layout()
# plt.savefig('movie_duration_histogram.png')
# plt.show()

# Release Year Vs Shows
# release_counts=df['Release_Year'].value_counts().sort_index()
# plt.scatter(release_counts.index,release_counts.values,color='red')
# plt.title('Release Year Vs No of Shows')
# plt.xlabel('Release Year')
# plt.ylabel('Number of Shows')
# plt.tight_layout()
# plt.grid()
# plt.savefig('release_year_scatter.png')
# plt.show()

# Top 10 country show
# country_counts=df['Country'].value_counts().head(10)
# plt.barh(country_counts.index,country_counts.values,color='teal')
# plt.title('Top 10 Countries by Number of Shows')
# plt.xlabel('No of Shows')
# plt.ylabel('Country')
# plt.tight_layout()
# # plt.grid()
# plt.savefig('top10_country.png')
# plt.show()

# Movie Vs Tv Shows by year
content_by_year=df.groupby(['Release_Year','Type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))

#first Subplot:movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='purple')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# Second Subplot:movies
ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='blue')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Movies')
fig.suptitle('Comparision of Moovies and TV Shows Released Over Year')
plt.tight_layout()
plt.savefig('movie_tv_shows comparision.png')
plt.show()
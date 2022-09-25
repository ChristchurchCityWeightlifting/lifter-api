/** @format */

import { Box } from "@mui/system";
import { useInfiniteQuery } from "react-query";
import React, { useCallback, useRef, useEffect } from "react";
import apiClient from "../../utils/http-common/http-common";
import { CompetitionListObjectProps } from "../../interfaces";
import CustomError from "../../components/Error";
import CustomLoading from "../../components/Loading";
import CompetitionCard from "./CompetitionCard";
import CompetitionRecentLoading from "./CompetitionRecentLoading";

const CompetitionRecent: React.FC = () => {
  const observerElem = useRef(null);

  const fetchRecentCompetitions = async (page: number) => {
    const PAGE_LIMIT = 10;
    const res = await apiClient.get(
      `/competitions?page=${page}&page_size=${PAGE_LIMIT}`
    );
    return res.data;
  };

  const {
    data,
    error,
    isLoading,
    isError,
    isSuccess,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useInfiniteQuery(
    ["recentCompetitions"],
    ({ pageParam = 1 }) => fetchRecentCompetitions(pageParam),
    {
      enabled: true,
      getNextPageParam: (lastPage, page) => {
        if (lastPage.next == null) {
          return undefined;
        }
        return page.length + 1;
      },
    }
  );

  const handleObserver: IntersectionObserverCallback = useCallback(
    (entries) => {
      const [target] = entries;
      if (target.isIntersecting && hasNextPage) {
        fetchNextPage();
      }
    },
    [fetchNextPage, hasNextPage]
  );

  useEffect(() => {
    const element = observerElem.current;
    const option = { threshold: 0 };

    const observer = new IntersectionObserver(handleObserver, option);
    observer.observe(element!);
    return () => observer.unobserve(element!);
  }, [fetchNextPage, hasNextPage, handleObserver]);

  if (isError) {
    console.log(error);
  }

  return (
    <>
      <Box
        sx={{
          display: "flex",
          flex: 1,
          gap: 2,
          justifyContent: "flex-start",
          alignItems: "flex-start",
          flexWrap: "wrap",
        }}
      >
        {isLoading && <CompetitionRecentLoading />}
        {isError && <CustomError />}
        {isSuccess && (
          <Box>
            {data?.pages.map((page) => (
              <React.Fragment key={page}>
                {page.results.map((competition: CompetitionListObjectProps) => (
                  <Box
                    sx={{
                      flexGrow: 0,
                      flexShrink: 0,
                      flexBasis: "31%",
                      alignSelf: "stretch",
                    }}
                    key={competition.reference_id}
                  >
                    <CompetitionCard
                      referenceId={competition.reference_id}
                      name={competition.name}
                      liftCount={competition.lifts_count}
                      dateStart={competition.date_start}
                      dateEnd={competition.date_end}
                      randomLifts={competition.random_lifts}
                    />
                  </Box>
                ))}
              </React.Fragment>
            ))}
          </Box>
        )}
      </Box>
      <Box ref={observerElem}>
        {isFetchingNextPage && hasNextPage ? <CustomLoading /> : null}
      </Box>
    </>
  );
};

export default CompetitionRecent;
